import logging
from flask_restx import Namespace, Resource, abort
from models.task import Task
from services.task_service import get_all_tasks, get_task, create_task, update_task, delete_task
from utils.utils import generate_swagger_model
from werkzeug.exceptions import HTTPException, BadRequest, NotFound

# Initialize logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Namespace for tasks
tasks_ns = Namespace('task', description='CRUD operations for managing tasks')

# Generate the Swagger model for tasks
task_model = generate_swagger_model(
    api=tasks_ns,
    model=Task,
    exclude_fields=[],
    readonly_fields=['task_id', 'created_at']
)

# Routes for managing tasks
@tasks_ns.route('/')
@tasks_ns.response(500, 'Internal Server Error')
class TaskList(Resource):
    @tasks_ns.doc('get_all_tasks')
    @tasks_ns.marshal_list_with(task_model)
    def get(self):
        try:
            tasks = get_all_tasks()
            return tasks
        except HTTPException as http_err:
            raise http_err
        except Exception as e:
            logger.error(f"Error fetching all tasks: {e}")
            tasks_ns.abort(500, "Internal Server Error")

    @tasks_ns.doc('create_task')
    @tasks_ns.expect(task_model)
    @tasks_ns.marshal_with(task_model, code=201)
    @tasks_ns.response(400, 'Bad Request')
    def post(self):
        try:
            data = tasks_ns.payload
            task = create_task(
                description=data['description'],
                employee_id=data['employee_id'],
                start_date=data['start_date'],
                end_date=data['end_date'],
                status=data['status'],
                work_id=data['work_id']
            )
            return task, 201
        except HTTPException as http_err:
            raise http_err
        except Exception as e:
            logger.error(f"Error creating task: {e}")
            tasks_ns.abort(400, "Bad Request")


@tasks_ns.route('/<int:task_id>')
@tasks_ns.response(404, 'Task ID not found')
@tasks_ns.response(500, 'Internal Server Error')
@tasks_ns.param('task_id', 'Task ID')
class Task(Resource):
    @tasks_ns.doc('get_task')
    @tasks_ns.marshal_with(task_model)
    def get(self, task_id):
        try:
            task = get_task(task_id)
            if not task:
                tasks_ns.abort(404, f"Task with ID {task_id} not found.")
            return task
        except HTTPException as http_err:
            raise http_err
        except Exception as e:
            logger.error(f"Error fetching task {task_id}: {e}")
            tasks_ns.abort(500, "Internal Server Error")

    @tasks_ns.doc('update_task')
    @tasks_ns.expect(task_model)
    @tasks_ns.marshal_with(task_model)
    @tasks_ns.response(400, 'Bad Request')
    def put(self, task_id):
        try:
            data = tasks_ns.payload
            updated_task = update_task(
                task_id,
                description=data['description'],
                employee_id=data['employee_id'],
                start_date=data['start_date'],
                end_date=data['end_date'],
                status=data['status'],
                work_id=data['work_id']
            )
            if not updated_task:
                tasks_ns.abort(404, f"Task with ID {task_id} not found.")
            return updated_task
        except HTTPException as http_err:
            raise http_err
        except Exception as e:
            logger.error(f"Error updating task {task_id}: {e}")
            tasks_ns.abort(400, "Bad Request")

    @tasks_ns.doc('delete_task')
    def delete(self, task_id):
        try:
            deleted = delete_task(task_id)
            if not deleted:
                tasks_ns.abort(404, f"Task with ID {task_id} not found.")
            return '', 204
        except HTTPException as http_err:
            raise http_err
        except Exception as e:
            logger.error(f"Error deleting task {task_id}: {e}")
            tasks_ns.abort(500, "Internal Server Error")
