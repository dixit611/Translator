// translator/static/translator/js/speak.js

function getCookie(name) {
  let cookieValue = null;
  if (document.cookie && document.cookie !== '') {
      const cookies = document.cookie.split(';');
      for (let i = 0; i < cookies.length; i++) {
          const cookie = cookies[i].trim();
          if (cookie.substring(0, name.length + 1) === (name + '=')) {
              cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
              break;
          }
      }
  }
  return cookieValue;
}
const csrftoken = getCookie('csrftoken');

function translateText() {
  const text = document.getElementById('text').value;
  const srcLang = document.getElementById('src_lang').value;
  const destLang = document.getElementById('dest_lang').value;

  if (!text || !srcLang || !destLang) {
      document.getElementById('translated-text').innerText = 'Error: Please fill in all fields.';
      return;
  }

  fetch('/translate/', {
      method: 'POST',
      headers: {
          'Content-Type': 'application/json',
          'X-CSRFToken': csrftoken
      },
      body: JSON.stringify({
          'text': text,
          'src_lang': srcLang,
          'dest_lang': destLang
      })
  })
  .then(response => response.json())
  .then(data => {
      if (data.translated_text) {
          document.getElementById('translated-text').innerText = data.translated_text;
      } else if (data.error) {
          document.getElementById('translated-text').innerText = `Error: ${data.error}`;
      }
  })
  .catch(error => {
      console.error('Error:', error);
      document.getElementById('translated-text').innerText = 'Error: Something went wrong.';
  });
}

function speakText() {
  const text = document.getElementById('translated-text').innerText;
  if (responsiveVoice.voiceSupport()) {
      responsiveVoice.speak(text);
  } else {
      alert("Sorry, your browser doesn't support text to speech!");
  }
}
