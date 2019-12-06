<template>
  <footer class="footer" style="bottom:0;position:absolute;width:100%;">
    <div class="container-fluid d-flex flex-wrap justify-content-between">
      <nav>
        <ul>
          <li>
            <router-link :to="{path:'/admin'}">Dashboard</router-link>
          </li>
        </ul>
      </nav>
      <div class="copyright d-flex flex-wrap">
        NuveaPaaS Copyright 2019
      </div>
    </div>
  </footer>
</template>
