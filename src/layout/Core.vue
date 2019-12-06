<template>
  <div class="wrapper">
    <side-bar>
      <template slot="links">
        <sidebar-link to="/documents" name="Mes documents" icon=""/> <!-- TODO Add logo-->
        <sidebar-link to="/map" name="Map" icon=""/> <!-- TODO Add logo-->
      </template>
    </side-bar>
    <div class="main-panel">
      <top-bar />
      <page-content @click.native="toggleSidebar" />
      <page-footer />
    </div>
    <chat></chat>

  </div>
</template>
<style lang="scss">
</style>
<script>
import TopBar from "./TopBar.vue";
import PageFooter from "./PageFooter.vue";
import PageContent from "./PageContent.vue";
import Chat from '@/components/Chat/Chat.vue';

export default {
  components: {
    PageFooter,
    PageContent,
    TopBar,
    Chat,
  },
  methods: {
    toggleSidebar() {
      if (this.$sidebar.showSidebar) {
        this.$sidebar.displaySidebar(false);
      }
    }
  }
};
</script>
