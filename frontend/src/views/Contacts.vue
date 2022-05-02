<template>
  <div class="contacts_block">
    <br>
    <h2>Наши контакты</h2>
    <br>
    <div class="contacts">
      <div v-for="contact in contacts" :key="contact.id" class="contact_block">
        <div class="contact_first_name" style="font-size: 22px;">
            {{contact.first_name}}
        </div>
        <div class="contact_last_name" style="font-size: 22px;">
          {{contact.last_name}}
        </div>
        <div class="contact_phone" style="font-size: 22px;">
          {{contact.phone}}
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  name: "Contacts",
  data() {
    return {
      contacts: []
    }
  },
  created() {
        this.getContacts()
    },
    methods:{
        getContacts(){
            axios.get(
                'http://localhost:8000/api/users/',{
            }).then((response) =>{
                this.contacts = response.data

            }).catch((err)=>{
                console.log(err)
            })
        },
      }
}
</script>

<style scoped>
  .contacts{
    width: 1000px;
    margin: 0 auto;
  }
  .contact_block{
    display: flex;
    border: 2px solid rgb(102, 0, 0);
    padding: 5px;
    border-radius: 5px;
    margin-top: 15px;
    flex-direction: row;
    gap: 30px;
    align-items: center;
    justify-content: center;
  }
</style>