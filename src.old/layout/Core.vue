<template>
  <div>
      <side-bar />
      <top-bar />
      <page-content/>
      <page-footer />
  </div>
</template>
<script>
import SideBar from "./SideBar.vue";
import TopBar from "./TopBar.vue";
import PageFooter from "./PageFooter.vue";
import PageContent from "./PageContent.vue";
export default {
  components: {
    SideBar,
    PageFooter,
    PageContent,
    TopBar,
  }
  };
</script>
