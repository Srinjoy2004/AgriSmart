
  // Get modal instances
  const modal1 = new bootstrap.Modal(document.getElementById('modal1'));
  const modal2 = new bootstrap.Modal(document.getElementById('modal2'));

  // Switch from Modal 1 to Modal 2
  document.getElementById('switchToModal2').addEventListener('click', () => {
    modal1.hide(); // Close Modal 1
    modal2.show(); // Open Modal 2
  });

  // Switch from Modal 2 to Modal 1
  document.getElementById('switchToModal1').addEventListener('click', () => {
    modal2.hide(); // Close Modal 2
    modal1.show(); // Open Modal 1
  });
