import Core from "@/layout/Core.vue";
// GeneralViews
import NotFound from "@/pages/NotFound.vue";
import Marketplace from "@/pages/Marketplace.vue";
import Detail from "@/pages/Detail.vue";
import Cart from "@/pages/Cart.vue";
import Documents from "@/pages/Documents.vue";
import Document from "@/components/Document/Document.vue";
import Map from "@/pages/Map.vue";

const routes = [
  {
    path: "/",
    redirect: "/documents",
    name: "home",
    component: Core,
    children: [
      {
        path: "map",
        name: "Map",
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
