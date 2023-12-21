import Vue from 'vue'
import VueRouter from 'vue-router'
import FormulaOne from '@/components/FormulaOne'
import FormulaOne_Qualifying from '@/components/FormulaOne_Qualifying'
import FormulaOne_Final from '@/components/FormulaOne_Final'
import FormulaOne_Point from '@/components/FormulaOne_Point'
import FormulaOne_Driver from '@/components/FormulaOne_Driver'

Vue.use(VueRouter)

const routes = [
  { path: '/', name: 'FormulaOne', component: FormulaOne },
  { path: '/qualifying', name: 'FormulaOne_Qualifying', component: FormulaOne_Qualifying },
  { path: '/final', name: 'FormulaOne_Final', component: FormulaOne_Final },
  { path: '/point', name: 'FormulaOne_Point', component: FormulaOne_Point },
  { path: '/driver', name: 'FormulaOne_Driver', component: FormulaOne_Driver },
]

const router = new VueRouter({
  routes,
  mode: 'history',
})

export default router
