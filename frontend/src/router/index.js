import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'
import ServiceType from '../views/ServicePage.vue'
import Repairs from "@/views/Repairs";
import ServicesPage from '@/views/Services'
import AvtoElectric from '@/views/AvtoElectric'
import ServiceOrder from '@/views/ServiceOrder'
import Contacts from '@/views/Contacts'


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
  },
  {
    path: "/services",
    name: "ServicesPage",
    component: ServicesPage
  },
  {
    path: '/electric',
    name: "AvtoElectric",
    component: AvtoElectric
  },
  {
    path: '/order',
    name: 'ServiceOrder',
    component: ServiceOrder
  },
  {
    path: '/contacts',
    name: 'Contacts',
    component: Contacts
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
