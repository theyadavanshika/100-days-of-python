from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///tasks.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)


class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    completed = db.Column(db.Boolean, default=False)


with app.app_context():
    db.create_all()


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        task_title = request.form.get("task", "").strip()

        if task_title:
            new_task = Todo(title=task_title)
            db.session.add(new_task)
            db.session.commit()

        return redirect(url_for("home"))

    all_tasks = (
        db.session.execute(db.select(Todo).order_by(Todo.id.desc())).scalars().all()
    )

    total_tasks = len(all_tasks)
    completed_tasks = sum(1 for task in all_tasks if task.completed)
    pending_tasks = total_tasks - completed_tasks

    return render_template(
        "index.html",
        tasks=all_tasks,
        total_tasks=total_tasks,
        completed_tasks=completed_tasks,
        pending_tasks=pending_tasks,
    )


@app.route("/complete/<int:task_id>", methods=["POST"])
def complete_task(task_id):
    task = db.get_or_404(Todo, task_id)
    task.completed = not task.completed
    db.session.commit()
    return redirect(url_for("home"))


@app.route("/delete/<int:task_id>", methods=["POST"])
def delete_task(task_id):
    task = db.get_or_404(Todo, task_id)
    db.session.delete(task)
    db.session.commit()
    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True)
