<template>
  <div class="services-block">
      <h2 class="services__title">
        АВТОЭЛЕКТРИКА
      </h2>

      <div class="services">
          <div class="electric_block" v-for="item in items" :key="item.id">
              <div class="service_image" @mouseleave="hideSuggestions($event)" @mouseover="showSuggestions($event)">
                <img v-if="item.images.length == 0" width="350" class="image_service" src="~@/assets/avto-service-logo.jpeg" alt="">
                <img v-else width="350" height="310" class="image_service" :src="'http://localhost:8000/media/'+item.images[0]" alt="">
                <div class="service_suggestions" align="left" style="pointer-events: none">
                    <ul class=ul_suggestions>
                        <li class="li_suggestion" v-for="i in 6" :key="i">{{item.suggestions[i]}}</li>
                    </ul>
                </div>
              </div>
            <div class="service_title" @click="toServicePage(item.id)">
                {{item.title}}
            </div>
            <div class="service_type">
                {{item.get_type_display}}
            </div>
            <div class="service_preview_text" align="left">
                {{item.preview_text}}
            </div>
          </div>

      </div>
  </div>
</template>

<script>
import axios from 'axios'
export default {
    name: 'AvtoElectric',
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
        getAllItems(){
            axios.get(
                'http://localhost:8000/api/services/',{
                params: {
                    type: 'electric'
                }
            }).then((response) =>{
                this.items = response.data
                this.items.forEach(element => {
                  element.preview_text = element.preview_text.slice(0, 160) + '...'
                });

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
    top: 30px;
}
.services__title{
    align-items: center;
    margin-bottom: 30px;
}

.services{
    display: flex;
    flex-direction: row;
    margin: 0 auto;
    width: 1200px;
    flex-wrap: wrap
}
.electric_block{
    border: 2px solid #880000;
    margin: 10px;
    border-radius: 5px;
    margin-bottom: 20px;
    width: 380px;

}

.service_image{
    border-bottom: 2px solid #8a0000;
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

.service_preview_text{
  font-size: 15px;
  padding: 10px;
}
</style>