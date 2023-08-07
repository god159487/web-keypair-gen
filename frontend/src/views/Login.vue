<template>
  <div class="container">
    <div class="row justify-content-center">
      <div class="col-md-10">
        <div class="card">
          <h5 class="card-header">Login</h5>
          <div class="card-body">
            <form action="#" @submit.prevent="Login">
              <div class="form-group row">
                <label for="email" class="col-md-4 col-form-label text-md-right"
                  >Email</label
                >
                <div class="col-md-6">
                  <input
                    id="email"
                    type="email"
                    placeholder="Enter your email"
                    class="form-control"
                    name="email"
                    value
                    required
                    autofocus
                    v-model="email"
                  />
                </div>
              </div>

              <div class="form-group row mt-3">
                <label
                  for="password"
                  class="col-md-4 col-form-label text-md-right"
                  >Password</label
                >
                <div class="col-md-6">
                  <input
                    id="password"
                    type="password"
                    placeholder="Enter your password"
                    class="form-control"
                    name="password"
                    required
                    v-model="password"
                  />
                </div>
              </div>

              <div class="form-group row mb-0 mt-3">
                <div class="col-md-8 offset-md-4">
                  <button type="submit" class="btn btn-primary">Login</button>
                </div>
              </div>
            </form>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>


<script>
import { ref } from "vue";
import { useStore } from "vuex";
import { useRouter } from "vue-router";
import { useLoading } from "vue-loading-overlay";
import { toast } from 'vue3-toastify';
import 'vue3-toastify/dist/index.css';

export default {
  name: "LoginComponent",
  setup() {
    const email = ref("");
    const password = ref("");
    const error = ref(null);
    const store = useStore();
    const router = useRouter();

    const Login = async () => {      
      const loader = $loading.show({
        // Optional parameters
      });
      try {
        await store.dispatch("logIn", {
          email: email.value,
          password: password.value,
        });
        loader.hide()
        router.push("/keypair");
      } 
      catch (err) {
        if (err.code === "auth/user-not-found") {
          error.value = "Username is not found";
          notify_error(error.value);
        } else if (err.code === "auth/wrong-password") {
          error.value = "Password is incorrect";
          notify_error(error.value);
        } else {
          error.value = "Please try again";
          notify_error(error.value);
        }
        loader.hide();
      }
    };

    const notify_error = (msg) => {
      toast.error(msg, {
        autoClose: 5000,
        position: toast.POSITION.BOTTOM_RIGHT,
      }); // ToastOptions
    }

    const $loading = useLoading({
      // options
    });

    return { Login, email, password, error };
  },
};
</script>
