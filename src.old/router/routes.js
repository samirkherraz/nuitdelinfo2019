import Core from "@/layout/Core.vue";
import NotFound from "@/pages/NotFound.vue";
import Index from "@/pages/Index.vue";
const routes = [
  {
    path: "/",
    component: Core,
    children: [
      {
        path: "index",
        name: "index",
        component: Index
      },
      { 
        path: "*",         
        name: "Error 404",
        component: NotFound 
      }
    ]
  }
];

export default routes;
