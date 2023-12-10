import Vue from 'vue'
import VueRouter from 'vue-router'
import FormulaOne from '@/components/FormulaOne'
import FormulaOne_Qualifying from '@/components/FormulaOne_Qualifying'

Vue.use(VueRouter)

const routes = [
    {path:'/',component: FormulaOne },
    { path: '/qualifying', component: FormulaOne_Qualifying }
  ]

  const router = new VueRouter({
    mode: 'history',
    routes
  })

  export default router