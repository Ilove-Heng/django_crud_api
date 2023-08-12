<template>
  <div class="container">
    <div class="row">
      <div class="col-sm-10">
        <h1>Tasks</h1>
        <hr/>
        <br/><br/>
        <alert v-if="showMessage" :message="message"></alert>
        <button
            class="btn btn-success btn-sm"
            type="button"
            @click="toggleAddBookModal">
          Add Task
        </button>
        <br/><br/>
        <table class="table table-hover">
          <thead>
          <tr>
            <th scope="col">ID</th>
            <th scope="col">name</th>
            <th scope="col">description</th>
            <th scope="col">Due Date</th>
            <th scope="col">Created by</th>
            <th></th>
          </tr>
          </thead>
          <tbody>
          <!-- <tr v-for="(book, index) in books" :key="index"> -->
          <tr v-for="(task, index) in tasks" :key="index">
            <!-- {{ task }} -->
            <td>{{ task.id }}</td>
            <td>{{ task.name }}</td>
            <td>{{ task.description }}</td>
            <td>{{ task.due_date }}</td>
            <td>{{ task.created_by_id }}</td>
            <td>
              <div class="btn-group" role="group">
                <button
                    class="btn btn-warning btn-sm"
                    type="button"
                    @click="toggleEditBookModal(task)">
                  Update
                </button>
                <button
                    class="btn btn-danger btn-sm"
                    type="button"
                    @click="handleDeleteBook(task)">
                  Delete
                </button>
              </div>
            </td>
          </tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>
  <!-- add new book modal -->
  <div
      ref="addBookModal"
      :class="{ show: activeAddBookModal, 'd-block': activeAddBookModal }"
      class="modal fade"
      role="dialog"
      tabindex="-1">
    <div class="modal-dialog" role="document">
      <div class="modal-content">
        <div class="modal-header">
          <h5 class="modal-title">Add a new Task</h5>
          <button
              aria-label="Close"
              class="close"
              data-dismiss="modal"
              type="button"
              @click="toggleAddBookModal">
            <span aria-hidden="true">&times;</span>
          </button>
        </div>
        <div class="modal-body">
          <form>
            <div class="mb-3">
              <label class="form-label" for="addBookTitle">Name test:</label>
              <input
                  id="addBookTitle"
                  v-model="addTaskForm.name"
                  class="form-control"
                  placeholder="Enter name"
                  type="text"/>
            </div>
            <div class="mb-3">
              <label class="form-label" for="addBookAuthor">Description:</label>
              <input
                  id="addBookAuthor"
                  v-model="addTaskForm.description"
                  class="form-control"
                  placeholder="Enter description"
                  type="text"/>
            </div>
            <div class="mb-3">
              <label class="form-label" for="addBookAuthor">due date:</label>
              <input
                  id="addBookAuthor"
                  v-model="addTaskForm.due_date"
                  class="form-control"
                  placeholder="Enter author"
                  type="date"/>
            </div>
            
            <div class="btn-group" role="group">
              <button
                  class="btn btn-primary btn-sm"
                  type="button"
                  @click="handleAddSubmit">
                Submit
              </button>
              <button
                  class="btn btn-danger btn-sm"
                  type="button"
                  @click="handleAddReset">
                Reset
              </button>
            </div>
            {{ addTaskForm.due_date }}
          </form>
        </div>
      </div>
    </div>
  </div>
  <div v-if="activeAddBookModal" class="modal-backdrop fade show"></div>
  <!-- edit book modal -->
  <div
      ref="editBookModal"
      :class="{ show: activeEditBookModal, 'd-block': activeEditBookModal }"
      class="modal fade"
      role="dialog"
      tabindex="-1">
    <div class="modal-dialog" role="document">
      <div class="modal-content">
        <div class="modal-header">
          <h5 class="modal-title">Update</h5>
          <button
              aria-label="Close"
              class="close"
              data-dismiss="modal"
              type="button"
              @click="toggleEditBookModal">
            <span aria-hidden="true">&times;</span>
          </button>
        </div>
        <div class="modal-body">
          <form>
            <div class="mb-3">
              <label class="form-label" for="editBookTitle">Name:</label>
              <input
                  id="editBookTitle"
                  v-model="editBookForm.name"
                  class="form-control"
                  placeholder="Enter name"
                  type="text">
            </div>
            <div class="mb-3">
              <label class="form-label" for="editBookAuthor">Description:</label>
              <input
                  id="editBookAuthor"
                  v-model="editBookForm.description"
                  class="form-control"
                  placeholder="Enter description"
                  type="text">
            </div>

            <div class="mb-3">
              <label class="form-label" for="editBookAuthor">due date:</label>
              <input
                  id="editBookAuthor"
                  v-model="editBookForm.due_date"
                  class="form-control"
                  placeholder="Enter author"
                  type="date">
            </div>
            <div class="btn-group" role="group">
              <button
                  class="btn btn-primary btn-sm"
                  type="button"
                  @click="handleEditSubmit">
                Submit
              </button>
              <button
                  class="btn btn-danger btn-sm"
                  type="button"
                  @click="handleEditCancel">
                Cancel
              </button>
            </div>
          </form>
        </div>
      </div>
    </div>
  </div>
  <div v-if="activeEditBookModal" class="modal-backdrop fade show"></div>
</template>

<script>
import Alert from "./Alert.vue";

export default {
  data() {
    return {
      activeAddBookModal: false,
      addTaskForm: {
        id: "",
        name: "",
        description: "",
        due_date: "",
      },
      activeEditBookModal: false,
      editBookForm: {
        id: "",
        name: "",
        description: "",
        due_date: "",
      },
      // books: [],
      tasks: [],
      message: "",
      showMessage: false,
    };
  },
  components: {
    alert: Alert,
  },
  methods: {
    addBook(payload) {
      console.log("🚀  payload:", payload)
      const path = "http://localhost:8000/viewsets/";
      this.$axios
          .post(path, payload)
          .then(() => {
            // will change soon
            this.getBooks();
            this.message = "Task added";
            this.showMessage = true;
          })
          .catch((error) => {
            console.log(error);
            this.getBooks();
          });
    },
    // will change soon name fn
    getBooks() {
      const path = "http://127.0.0.1:8000/viewsets/";
      this.$axios
          .get(path)
          .then((res) => {
            console.log("🚀  res:", res)
            this.tasks = res.data;
          })
          .catch((error) => {
            console.error(error);
          });
    },
    handleAddReset() {
      this.initForm();
    },
    handleAddSubmit() {
      // return console.log('addTaskForm',this.addTaskForm)
      this.toggleAddBookModal();
      const payload = {
        name: this.addTaskForm.name,
        description: this.addTaskForm.description,
        due_date: this.addTaskForm.due_date,
      };
      this.addBook(payload);
      this.initForm();
    },
    initForm() {
      this.addTaskForm.name = "";
      this.addTaskForm.description = "";
      this.addTaskForm.due_date = "";
      // this.editBookForm.id = "";
      // this.editBookForm.title = "";
      // this.editBookForm.author = "";
      // this.editBookForm.read = [];
    },
    toggleAddBookModal() {
      const body = document.querySelector("body");
      this.activeAddBookModal = !this.activeAddBookModal;
      if (this.activeAddBookModal) {
        body.classList.add("modal-open");
      } else {
        body.classList.remove("modal-open");
      }
    },
    toggleEditBookModal(task) {
      console.log("🚀  task:", task)
      if (task) {
        this.editBookForm = task;
      }
      const body = document.querySelector("body");
      this.activeEditBookModal = !this.activeEditBookModal;
      if (this.activeEditBookModal) {
        body.classList.add("modal-open");
      } else {
        body.classList.remove("modal-open");
      }
    },
    handleEditSubmit() {
      this.toggleEditBookModal(null);
      const payload = {
        name: this.editBookForm.name,
        description: this.editBookForm.description,
        due_date: this.editBookForm.due_date,
      };
      this.updateBook(payload, this.editBookForm.id);
    },
    updateBook(payload, taskTD) {
      const path = `http://127.0.0.1:8000/viewsets/${taskTD}/`;
      this.$axios.patch(path, payload)
          .then(() => {
            this.getBooks();
            this.message = 'Task updated!';
            this.showMessage = true;
          })
          .catch((error) => {
            console.error(error);
            this.getBooks();
          });
    },
    handleEditCancel() {
      this.toggleEditBookModal(null);
      this.initForm();
      this.getBooks(); // why?
    },
    handleDeleteBook(task) {
      this.removeBook(task.id);
    },
    removeBook(taskID) {
      const path = `http://127.0.0.1:8000/viewsets/${taskID}/`;
      this.$axios.delete(path)
          .then(() => {
            this.getBooks();
            this.message = 'Task removed!';
            this.showMessage = true;
          })
          .catch((error) => {
            console.error(error);
            this.getBooks();
          });
    },
  },
  created() {
    this.getBooks();
  },
};
</script>
