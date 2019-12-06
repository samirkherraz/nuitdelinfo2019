<template>
  <div :class="'chatbox '+hidden">
    <div @click="toggleHidden" class="head">ChatBot</div>
    <div id="messages" class="messages">
      <p v-for="msg in messages" :class="msg.align" >{{ msg.content }}</p>
    </div>
    <input
      @change="sendMsg($event);"
      class="input"
      type="text"
      placeholder="posez un question ... "
    />
  </div>
</template>
<script>
export default {
  
  data() {
    return {
      messages: [],
      hidden: ""
    };
  },
  methods: {
    sendMsg(event) {
      let value = event.target.value;
      event.target.value = "";
      this.messages.push({ content: value, align: "right" });

      this.$orchestra.sendMsg(data => {
        this.messages.push({ content: data, align: "left" });
        setTimeout(this.scroll, 100);
      }, value);
    },
    scroll() {
      var container = this.$el.querySelector(".chatbox .messages");
      container.scrollTop = container.scrollHeight;
    },
    toggleHidden(){
        if (this.hidden == "")
            this.hidden = "hidden"
        else
            this.hidden = ""
    }
  }
};
</script>
<style>
.chatbox {
  z-index: 9999;
  width: 300px;
  height: 300px;
  background: #fff;
  border-radius: 5px;
  box-shadow: 0px 0px 10px #999;
  position: fixed;
  bottom: 0px;
  right: 10px;
  display: block;
  -webkit-transition: all 1s; /* Safari prior 6.1 */
  transition: all 1s;
}
.chatbox p {
  box-shadow: 0px 0px 10px #eee;
  border-radius: 5px;
  padding: 10px;
}
.chatbox p.left {
  text-align: left;
  background: #eee;
}
.chatbox p.right {
  text-align: right;
  background: #fff;
}
.hidden{
    bottom: -260px;
}
.chatbox .head {
  width: 100%;
  padding: 10px;
  border: none;
  background: #26f;
  border-radius: 5px 5px 0px 0px;
  color: #fff;
  box-shadow: 0px 0px 10px #999;
  position: absolute;
  top: 0px;
  box-shadow: 0px 0px 10px #999;
}
.chatbox .messages {
  display: block;
  margin-top: 40px;
  padding: 10px;
  height: 220px;
  overflow: auto;
}
.chatbox .input {
  width: 100%;
  padding: 10px;
  border: none;
  position: absolute;
  bottom: 0px;
  box-shadow: 0px 0px 10px #999;
}
</style>
