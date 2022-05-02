<template>
  <div class="nav-bar">
      <ul class="nav-bar-items">
        <li class="navitem">
          <a class="navlink" aria-current="page" href="/">ГЛАВНАЯ</a>
        </li>
        <li class="navitem">
          <a class="navlink" aria-current="page" href="/repairs">РЕМОНТ</a>
        </li>
        <li class="navitem">
          <a class="navlink" aria-current="page" href="/services">УСЛУГИ</a>
        </li>
        <li class="navitem">
          <a class="navlink" aria-current="page" href="/electric">АВТОЭЛЕКТРИКА</a>
        </li>
        <li class="navitem">
          <a class="navlink" aria-current="page" href="/order">ЗАКАЗ УСЛУГИ</a>
        </li>
        <li class="navitem">
          <a class="navlink" aria-current="page" href="/">О КОМПАНИИ</a>
        </li>
        <li class="navitem">
          <a class="navlink" aria-current="page" href="/contacts">КОНТАКТЫ</a>
        </li>
    
      </ul>
  </div>
</template>

<script>
export default {
    name: 'NavBar',

}
</script>

<style scoped>

.nav-bar-items{
    list-style-type: none;
    display: flex;
    width: 1100px;
    justify-content: space-between;
    align-items: center;
    margin: 0 auto;
    height: 100px;
    border: 1px solid gray;
    margin-top: 10px;
}

.navitem:last-child{
    margin-right: 30px;
}
</style>