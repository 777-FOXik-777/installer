<h1 align="center">Installer v3</h1>

<p align="center">
  <img src="https://img.shields.io/badge/Версия-3.0.0-cyan?style=flat-square">
  <img src="https://img.shields.io/badge/Написано%20на-Python-blue?style=flat-square">
  <img src="https://img.shields.io/badge/Поддерживается%3F-Да-green?style=flat-square">
</p>
<p align="center">
<a href="https://github.com/777-FOXik-777"><img title="Подпищиков" src="https://img.shields.io/github/followers/777-FOXik-777?color=red&style=flat-square"></a>
<a href="https://github.com/777-FOXik-777"><img title="Звезд" src="https://img.shields.io/github/stars/777-FOXik-777/installer?color=yellow&lstyle=flat-square"></a>
<a href="https://github.com/777-FOXik-777"><img title="Просмотры" src="https://img.shields.io/github/watchers/777-FOXik-777/installer?color=blue&style=flat-square"></a>
</p>

![Installer](https://github.com/777-oleg-777/test/blob/main/logo-installer.jpg)

<p align="center">
<a href="https://github.com/777-FOXik-777"><img title="Github" src="https://img.shields.io/badge/Github-777%7EFOXik%7E777-indigo?style=for-the-badge&logo=github"></a>
<a href="https://t.me/+1MZLhFv1sMJjZmFi"><img title="Telegram" src="https://img.shields.io/badge/Telegram-SYPEXHACK-blue?style=for-the-badge&logo=telegram"></a>
</p>


## [~] Описание:

***Installer - это мощный и удобный скрипт, который поможет тебе легко и быстро установить более 25 отличных хакерских утилит в Termux. Этот инструмент подходит для любого уровня опыта и НЕ требует наличия root-прав на твоем устройстве. С Installer ты сможешь расширить свои возможности в Termux и получить доступ к различным инструментам для сканирования, анализа, взлома и тестирования безопасности.***


## [√] Установка на [Android](https://wikipedia.org/wiki/Android) [![alt tag](https://cdn1.iconfinder.com/data/icons/logotypes/32/android-32.png)](https://fr.wikipedia.org/wiki/Android)
 
Скачиваем [Termux](https://t.me/SYPEXHACK_fail/51) (0.118)

### [+] Обновляем пакеты:

```
apt update
apt upgrade -y
``` 

### [+] Установка зависимостей:

```
pkg install git
pkg install python -y
``` 

### [+] Установка Installer:

``` 
git clone https://github.com/777-FOXik-777/installer
cd installer
python installer.py
``` 

Дальше Installer сделает все за вас: он установит все необходимые компоненты и обеспечит тебе доступ ко всему функционалу.

<h1 align="center">Снимок некоторых возможностей:</h1>

![Installer](https://github.com/777-oleg-777/test/blob/main/1present.jpg)

## [√] Для повторного запуска:

```
cd ~/installer
python installer.py
``` 
Альтернатива:
``` 
installer
``` 

## [?] Решение типичных проблем:

- При первом использовании тунелирования, если вы не получаете ссылку, введите "yes" (без кавычек) и нажмите Enter, чтобы получить ссылку.
- VPN или прокси препятствуют туннелированию и даже нормальному доступу в Интернет. Отключите их, если у вас возникли проблемы.
- Некторые утилиты на старых версия Installer могут некорректно или вовсе не работать. Обновите Installer до последней версии для более комфортного использования.
- Termux из Google Play может некорректно работать. Советую скачать оптимальную версию [Termux](https://t.me/SYPEXHACK_fail/51) (0.118)
- Если утилита не запускается но пишет "<Утилита> уже установлена!", то её необходимо удалить в настройках Installer. После этого утилиту можно заново запустить.

## [~] Полезное:

- ### [Добавить утилиту в Installer](https://forms.gle/vMHny8Yp24HQZqLV9)
- ### [Другие версии Installer](https://github.com/777-FOXik-777/installer/releases)
- ### [Обсуждение Installer](https://github.com/777-FOXik-777/installer/discussions)
- ### [Сообщить об ошибке](https://t.me/SYPEXHACK_help_bot)

## [~] Подпишись на:

- [![Github](https://img.shields.io/badge/Github-777%7EFOXik%7E777-indigo?style=for-the-badge&logo=github)](https://github.com/777-FOXik-777)


- [![Telegram](https://img.shields.io/badge/Telegram-SYPEXHACK-blue?style=for-the-badge&logo=telegram)](https://t.me/+1MZLhFv1sMJjZmFi)
##

> [!WARNING]\
> Этот инструмент создан с целью обучения и повышения квалификации в области хакинга и безопасности. Некоторые утилиты, фото, и другие файлы, которые используются в этом инструменте, взяты из открытых источников и принадлежат их законным авторам. Разработчик не несет ответственности за неправомерное использование этого инструмента и уважает права и интересы законных авторов.







<!DOCTYPE html>
<html>
<head>
  <style>
    .carousel {
      display: flex;
      overflow: hidden;
      width: 300px; /* Укажите нужную ширину */
    }

    .carousel img {
      width: 100%;
      transition: transform 0.5s ease-in-out;
    }

    #prevBtn, #nextBtn {
      cursor: pointer;
      position: absolute;
      top: 50%;
      transform: translateY(-50%);
      font-size: 24px;
      color: white;
      background-color: black;
      border: none;
      padding: 10px;
      z-index: 1;
    }

    #prevBtn { left: 0; }
    #nextBtn { right: 0; }
  </style>
</head>
<body>

<div class="carousel">
  <button id="prevBtn" onclick="prevSlide()">❮</button>
  <img src="image1.jpg" alt="Image 1">
  <img src="image2.jpg" alt="Image 2">
  <img src="image3.jpg" alt="Image 3">
  <!-- Добавьте больше изображений по необходимости -->
  <button id="nextBtn" onclick="nextSlide()">❯</button>
</div>

<script>
  let currentSlide = 0;

  function showSlide(index) {
    const carousel = document.querySelector('.carousel');
    const slideWidth = carousel.clientWidth;
    const newTransformValue = -index * slideWidth + 'px';
    carousel.style.transform = 'translateX(' + newTransformValue + ')';
    currentSlide = index;
  }

  function nextSlide() {
    currentSlide = (currentSlide + 1) % document.querySelectorAll('.carousel img').length;
    showSlide(currentSlide);
  }

  function prevSlide() {
    currentSlide = (currentSlide - 1 + document.querySelectorAll('.carousel img').length) % document.querySelectorAll('.carousel img').length;
    showSlide(currentSlide);
  }
</script>

</body>
</html>
