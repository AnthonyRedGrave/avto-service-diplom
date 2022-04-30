import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'
import ServiceType from '../views/ServicePage.vue'
import Repairs from "@/views/Repairs";


const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/service',
    name: 'ServiceType',
    component: ServiceType
  },
  {
    path: "/repairs",
    name: "Repairs",
    component: Repairs
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
