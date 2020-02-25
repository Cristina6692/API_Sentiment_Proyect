# API_Sentiment_Proyect

Hemos creado una API con usuarios y chats con conversaciones, con la que en el futuro podremos analizar os sentimientos de esos mensajes y recomendar unos usuarios a otros según afinidad.

Para introducir usuarios en la base de datos: 

 --Utilizamos la ruta @app.route('/insert/user/ <u_name>')
 
Para introducir un nuevo chat:

 --Utilizamos la ruta @app.route('/insert/chat/<ChatName>')
  
Para introducir un nuevo usuario a un chat:

 --Utilizamos la ruta @app.route('/insert/userMessageInChat/<ChatID>') y los parametros 'user_name' y 'texto
  
