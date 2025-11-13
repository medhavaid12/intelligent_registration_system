const form = document.getElementById('regForm');
const submitBtn = document.getElementById('submitBtn');
const resultMsg = document.getElementById('resultMsg');

form.addEventListener('input', () => {
  const valid = form.checkValidity();
  submitBtn.disabled = !valid;
});

form.addEventListener('submit', (e) => {
  e.preventDefault();
  if (!form.checkValidity()) {
    resultMsg.innerHTML = '<span class="error">Please fill all required fields correctly.</span>';
  } else {
    resultMsg.innerHTML = '<span class="success">Registration Successful! Your profile has been submitted successfully.</span>';
    form.reset();
    submitBtn.disabled = true;
  }
});
