Репозиторий интернет-магазина на Django 3.

<!—Подключаем клиента Braintree. -->
 <script src="https://js.braintreegateway.com/web/3.29.0/js/client.min.js"></script>
 <!—Подключаем компонент Hosted Fields. -->
 <script src="https://js.braintreegateway.com/web/3.29.0/js/hosted-
 fields.min.js"></script>
 <script>
 var form = document.querySelector('#payment');
 var submit = document.querySelector('input[type="submit"]');
 braintree.client.create({
 authorization: '{{ client_token }}'
 }, function (clientErr, clientInstance) {
 if (clientErr) {
 console.error(clientErr);
 return;
 }
 braintree.hostedFields.create({
 client: clientInstance,
 styles: {
 'input': {'font-size': '13px'},
 'input.invalid': {'color': 'red'},
 'input.valid': {'color': 'green'}
 },
 fields: {
 number: {selector: '#card-number'},
 cvv: {selector: '#cvv'},
 expirationDate: {selector: '#expiration-date'}
 }
 }, function (hostedFieldsErr, hostedFieldsInstance) {
 if (hostedFieldsErr) {
 console.error(hostedFieldsErr);
 return;
 }
 submit.removeAttribute('disabled');
 form.addEventListener('submit', function (event) {
 event.preventDefault();
 hostedFieldsInstance.tokenize(function (tokenizeErr, payload) {
 if (tokenizeErr) {
 console.error(tokenizeErr);
 return;
 }
 // Задаем значение поля для отправки токена на сервер.
 document.getElementById('nonce').value = payload.nonce;
 // Отправляем форму на сервер.
 document.getElementById('payment').submit();
 });
 }, false);
 });
 });
 </script>
