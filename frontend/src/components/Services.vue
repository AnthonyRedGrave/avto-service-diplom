<template>
  <div class="services-block">
      <h2 class="services__title">
        НАШИ УСЛУГИ
      </h2>
      <div class="services_nav_filters">
          <ul class="services_nav_items" style="cursor: pointer">
              <li class="services_nav_item" @click="getAllItems('')">Все</li>
              <li class="services_nav_item" @click="getAllItems('service')">Услуги</li>
              <li class="services_nav_item" @click="getAllItems('repair')">Ремонт</li>
              <li class="services_nav_item" @click="getAllItems('electric')">Автоэлектрика</li>
              <li class="services_nav_item" @click="showShop">Магазин</li>
          </ul>
      </div>
      <div class="services">
          <div class="service_block" v-for="item in items" :key="item.id">
              <div class="service_image" @mouseleave="hideSuggestions($event)" @mouseover="showSuggestions($event)">
                <img v-if="item.images.length == 0" width="350" class="image_service" src="~@/assets/avto-service-logo.jpeg" alt="">
                <img v-else width="350" height="310" class="image_service" :src="'http://localhost:8000/media/'+item.images[0]" alt="">
                <div class="service_suggestions" align="left" style="pointer-events: none">
                    <ul class=ul_suggestions>
                        <li class="li_suggestion" v-for="i in 5" :key="i">{{item.suggestions[i]}}</li>
                    </ul>
                </div>
              </div>
            <div class="service_title" @click="toServicePage(item.id)">
                {{item.title}}
            </div>
            <div class="service_type">
                {{item.get_type_display}}
            </div>
          </div>
          
      </div>
  </div>
</template>

<script>
import axios from 'axios'
export default {
    name: 'Services',
    data(){
        return{
            items: [],
        }
    },
    created() {
        this.getAllItems()
    },
    methods:{
        toServicePage(id){
            console.log(id)
            this.$router.push({ name: 'ServiceType', query: {'id': id }})
        },
        getAllItems(filter){
            axios.get(
                'http://localhost:8000/api/services/',{
                params: {
                    type: filter
                }
            }).then((response) =>{
                this.items = response.data
                
            }).catch((err)=>{
                console.log(err)
            })
        },
        showSuggestions(element){
            if (element.target.className == 'image_service'){
                let sugg_el = element.target.nextSibling
                sugg_el.style.opacity = 100
            }
            else if(element.target.className == "service_image"){
                let sugg_el = element.target.lastChild
                sugg_el.style.opacity = 100
            }
            
        },
        hideSuggestions(element){
            if (element.target.className == 'image_service'){
                let sugg_el = element.target.nextSibling
                sugg_el.style.opacity = 0
            }
            else if(element.target.className == "service_image"){
                let sugg_el = element.target.lastChild
                sugg_el.style.opacity = 0
            }
        }
    }
}
</script>

<style scoped>
.services-block{
    position: relative;
    top: 1500px;
}
.services__title{
    border-bottom: 1px solid red;
    align-items: center;
    margin-bottom: 30px;
}
.services_nav_items{
    list-style-type: none;
    display: flex;
    flex-direction: row;
    margin: 0 auto;
    margin-bottom: 50px;
    justify-content: space-between;
    width: 600px;
    gap: 30px;
}

.services_nav_item{
    border: 1px solid red;
    padding: 8px;
    border-radius: 5px;
}

.services{
    display: flex;
    flex-direction: row;
    margin: 0 auto;
    width: 1260px;
    flex-wrap: wrap
}
.service_block{
    display: block;
    border: 1px solid black;
    margin: 10px;
    border-radius: 15px;
    margin-bottom: 20px;
    width: 380px;
    
}

.service_image{
    border-bottom: 1px solid gray;
    position: relative;
    text-align: center;
}

.image_service{
    transition:opacity 500ms
}

.image_service:hover{
    opacity:0.15
}

.service_title{
    color: rgb(255, 72, 72);
    font-size: 20px;
}

.service_suggestions{
    position: absolute;
    top: 10%;
    opacity: 0;
    transition:opacity 500ms
}


.ul_suggestions{
    list-style-type: none;
    font-size: 18px;
    font-weight: bold;
    
}

.li_suggestion{
    margin: 10px 0;
}



.service_type{
    color: #424242;
}

.services_nav_item:hover{
    background-color: #fff7f7;
}

.services_nav_item:active{
    background-color: #dda2a2;
}
</style>