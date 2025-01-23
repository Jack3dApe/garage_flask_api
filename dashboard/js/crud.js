async function fetchClients() {
  try {
    const clients = await getClients();
    const tableBody = document.getElementById("clientsTableBody");

    tableBody.innerHTML = "";

    clients.forEach((client) => {
      const row = document.createElement("tr");
      row.innerHTML = `
        <td>${client.client_id}</td>
        <td>${client.name}</td>
        <td>${client.email}</td>
        <td>
          <button onclick="deleteClient(${client.client_id})"  class="btn btn-danger btn-sm"><svg  xmlns="http://www.w3.org/2000/svg"  width="24"  height="24"  viewBox="0 0 24 24"  fill="none"  stroke="currentColor"  stroke-width="2"  stroke-linecap="round"  stroke-linejoin="round"  class="icon icon-tabler icons-tabler-outline icon-tabler-trash"><path stroke="none" d="M0 0h24v24H0z" fill="none"/><path d="M4 7l16 0" /><path d="M10 11l0 6" /><path d="M14 11l0 6" /><path d="M5 7l1 12a2 2 0 0 0 2 2h8a2 2 0 0 0 2 -2l1 -12" /><path d="M9 7v-3a1 1 0 0 1 1 -1h4a1 1 0 0 1 1 1v3" /></svg>
          Delete</button>
        </td>
      `;
      tableBody.appendChild(row);
    });
  } catch (error) {
    console.error("Error fetching and displaying clients:", error);
  }
}

async function fetchEmployees() {
  try {
    const employees = await getEmployees();
    const tableBody = document.getElementById("employeesTableBody");

    tableBody.innerHTML = "";

    employees.forEach((employee) => {
      const row = document.createElement("tr");
      row.innerHTML = `
        <td>${employee.employee_id}</td>
        <td>${employee.name}</td>
        <td>${employee.email}</td>
        <td>${employee.role}</td>
        <td>
          <button onclick="deleteEmployee(${employee.employee_id})" class="btn btn-danger btn-sm">
            <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="icon icon-tabler icon-tabler-trash">
              <path stroke="none" d="M0 0h24v24H0z" fill="none"/>
              <path d="M4 7l16 0" />
              <path d="M10 11l0 6" />
              <path d="M14 11l0 6" />
              <path d="M5 7l1 12a2 2 0 0 0 2 2h8a2 2 0 0 0 2 -2l1 -12" />
              <path d="M9 7v-3a1 1 0 0 1 1 -1h4a1 1 0 0 1 1 1v3" />
            </svg> Delete
          </button>
        </td>
      `;
      tableBody.appendChild(row);
    });
  } catch (error) {
    console.error("Error fetching and displaying employees:", error);
  }
}

async function fetchWorks() {
  try {
    const works = await getWorks();
    const tableBody = document.getElementById("worksTableBody");

    tableBody.innerHTML = "";

    works.forEach((work) => {
      const row = document.createElement("tr");
      row.innerHTML = `
        <td>${work.work_id}</td>
        <td>${work.description}</td>
        <td>${work.cost}</td>
        <td>
          <button onclick="deleteWork(${work.work_id})" class="btn btn-danger btn-sm">
            <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="icon icon-tabler icon-tabler-trash">
              <path stroke="none" d="M0 0h24v24H0z" fill="none"/>
              <path d="M4 7l16 0" />
              <path d="M10 11l0 6" />
              <path d="M14 11l0 6" />
              <path d="M5 7l1 12a2 2 0 0 0 2 2h8a2 2 0 0 0 2 -2l1 -12" />
              <path d="M9 7v-3a1 1 0 0 1 1 -1h4a1 1 0 0 1 1 1v3" />
            </svg> Delete
          </button>
        </td>
      `;
      tableBody.appendChild(row);
    });
  } catch (error) {
    console.error("Error fetching and displaying works:", error);
  }
}

async function fetchVehicles() {
  try {
    const vehicles = await getVehicles();
    const tableBody = document.getElementById("vehiclesTableBody");

    tableBody.innerHTML = "";

    vehicles.forEach((vehicle) => {
      const row = document.createElement("tr");
      row.innerHTML = `
        <td>${vehicle.vehicle_id}</td>
        <td>${vehicle.license_plate}</td>
        <td>${vehicle.brand}</td>
        <td>${vehicle.model}</td>
        <td>${vehicle.year}</td>
        <td>
          <button onclick="deleteVehicle(${vehicle.vehicle_id})" class="btn btn-danger btn-sm">
            <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="icon icon-tabler icon-tabler-trash">
              <path stroke="none" d="M0 0h24v24H0z" fill="none"/>
              <path d="M4 7l16 0" />
              <path d="M10 11l0 6" />
              <path d="M14 11l0 6" />
              <path d="M5 7l1 12a2 2 0 0 0 2 2h8a2 2 0 0 0 2 -2l1 -12" />
              <path d="M9 7v-3a1 1 0 0 1 1 -1h4a1 1 0 0 1 1 1v3" />
            </svg> Delete
          </button>
        </td>
      `;
      tableBody.appendChild(row);
    });
  } catch (error) {
    console.error("Error fetching and displaying vehicles:", error);
  }
}
