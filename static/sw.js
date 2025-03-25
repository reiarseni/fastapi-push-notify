self.addEventListener('push', function(event) {
  console.log('Evento push recibido:', event);
  let data = {};
  if (event.data) {
    data = event.data.json();
  }
  const title = data.title || 'Notificación';
  const options = {
    body: data.body || 'Has recibido una notificación.',
    icon: '/static/logo.png'  // Ruta a la imagen del logotipo
  };
  event.waitUntil(
    self.registration.showNotification(title, options)
  );
});

