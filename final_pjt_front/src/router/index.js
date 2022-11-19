import Vue from 'vue'
import VueRouter from 'vue-router'

import MovieView from '../views/movies/MovieView.vue'
import MovieDetailView from '../views/movies/MovieDetailView.vue'
import DiscoveryMovieView from '../views/movies/DiscoveryMovieView.vue'
import FinderMovieView from '../views/movies/FinderMovieView.vue'

import SignupView from '../views/accounts/SignUpView.vue'
import LoginView from '../views/accounts/LogInView.vue'
import ProfileView from '../views/accounts/ProfileView.vue'

Vue.use(VueRouter)

const routes = [

  {
    path: '/signup',
    name: 'SignupView',
    component: SignupView

  },
  {
    path: '/Login',
    name: 'LoginView',
    component: LoginView

  },
  {
    path: '/profile',
    name: 'ProfileView',
    component: ProfileView

  },

  {
    path: '/movies',
    name: 'MovieView',
    component: MovieView
  },
  {
    path: '/movies/:id',
    name: 'MovieDetailView',
    component : MovieDetailView,
  },
  {
    path: '/movies/:id/createreview',
    name: 'CreateReview',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../components/Movies/CreateReview.vue')
  },
  {
    path: '/signup',
    name: 'SignUpView',
    component: SignUpView
  },
  {
    path: '/login',
    name: 'LogInView',
    component: LogInView
  },
  {
    path: '/discovery',
    name: 'DiscoveryMovieView',
    component : DiscoveryMovieView,
  },
  {
    path: '/finder',
    name: 'FinderMovieView',
    component : FinderMovieView,
  },
]


const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
