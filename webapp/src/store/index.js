import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    authenticated: false,
    token: {},
    working: false,
  },
  mutations: {
    login(state, token) {
      state.authenticated = true;
      state.token = token;
    },
    logout(state) {
      state.authenticated = false;
      state.token = {};
    },
    working(state, working = true) {
      state.working = working;
    },
  },
  actions: {
  },
  modules: {
  }
})
