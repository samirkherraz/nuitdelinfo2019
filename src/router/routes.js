import Core from "@/layout/Core.vue";
// GeneralViews
import NotFound from "@/pages/NotFound.vue";
import Documents from "@/pages/Documents.vue";
import Demarches from "@/pages/Demarches.vue";
import Map from "@/pages/Map.vue";

const routes = [
  {
    path: "/",
    redirect: "/documents",
    name: "home",
    component: Core,
    children: [
      {
        path: "demarches",
        name: "demarches",
        component: Demarches
      },
      {
        path: "map",
        name: "map",
        component: Map
      },
      {
        path: "documents",
        name: "mes documents",
        component: Documents
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
