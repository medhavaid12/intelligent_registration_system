describe('Registration Form Automation', () => {
  it('Negative Scenario - Missing Last Name', () => {
    cy.visit('web/index.html');
    cy.get('#firstName').type('John');
    cy.get('#email').type('john@example.com');
    cy.get('#phone').type('+911234567890');
    cy.get('input[value="Male"]').check();
    cy.get('#password').type('Pass@123');
    // button should be disabled when required fields are missing
    cy.get('#submitBtn').should('be.disabled');
    // submit the form programmatically to trigger validation message
    cy.get('form#regForm').then(($f) => {
      $f[0].dispatchEvent(new Event('submit', { cancelable: true, bubbles: true }));
    });
    cy.contains('Please fill all required fields').should('exist');
    cy.screenshot('error-state');
  });

  it('Positive Scenario - Successful Submission', () => {
    cy.visit('web/index.html');
    cy.get('#firstName').type('John');
    cy.get('#lastName').type('Doe');
    cy.get('#email').type('john@example.com');
    cy.get('#phone').type('+911234567890');
    cy.get('input[value="Male"]').check();
    cy.get('#password').type('Pass@123');
    cy.get('#submitBtn').click();
    cy.contains('Registration Successful').should('exist');
    cy.screenshot('success-state');
  });
});
