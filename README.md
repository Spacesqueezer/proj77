**1.** Уставнока ***gunicorn*** в проект через ***pip install gunicorn***

**2.** Создание службы для автозапуска сайта через ***sudo nano /etc/systemd/system/proj77.service***. Конфиг:
[![](https://i.ibb.co/mBkWjJ8/serv.png)](https://i.ibb.co/mBkWjJ8/serv.png)

**3.** Создание сокета через ***sudo nano /etc/systemd/system/proj77.socket***. Конфиг:
[![](https://i.ibb.co/0ym9q8N/sock.png)](https://i.ibb.co/0ym9q8N/sock.png)

**4.** Добавляем в автозапуск: ***sudo systemctl enable proj77***

**5.** Устанавливаем ***Nginx***: ***sudo apt install nginx***

**6.** Настраиваем ***Nginx*** через ***sudo nano /etc/nginx/sites-available/proj77***. Конфиг:
[![](https://i.ibb.co/8M3NBmd/nginx.png)](https://i.ibb.co/8M3NBmd/nginx.png)

**7.** Активируем серверные блоки: ***sudo ln -s /etc/nginx/sites-available/proj77 /etc/nginx/sites-enabled***

### Внешний вид сайта:
##### Страница добавления имён:
[![](https://i.ibb.co/3hwvdgW/1st.png)](https://i.ibb.co/3hwvdgW/1st.png)

##### Страница вывода:
[![](https://i.ibb.co/DzDC4pr/2nd.png)](https://i.ibb.co/DzDC4pr/2nd.png)
