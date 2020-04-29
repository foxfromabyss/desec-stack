import axios from 'axios';
import TimeAgo from 'javascript-time-ago';
import en from 'javascript-time-ago/locale/en';
import store from './store';

export const HTTP = axios.create({
  baseURL: '/api/v1/',
  headers: {
  },
});

export function logout() {
  try {
    HTTP.post('auth/logout/');
  } catch (e) {
    // TODO improve error handling
    // console.log(e)
  }
  store.commit('logout');
  HTTP.defaults.headers.common.Authorization = '';
  sessionStorage.removeItem('token');
}

TimeAgo.locale(en);
export const timeAgo = new TimeAgo();
