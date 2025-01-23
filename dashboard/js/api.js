const API_BASE_URL = "http://127.0.0.1:5000/api";

// GET de todos os clients
async function getClients() {
  try {
    const response = await fetch(`${API_BASE_URL}/client/`);
    if (!response.ok) {
      throw new Error(`API error: ${response.status} - ${response.statusText}`);
    }
    return await response.json();
  } catch (error) {
    console.error("Error fetching clients:", error);
    return [];
  }
}

// Apagar cliente
async function deleteClient(client_id) {
  try {
    const response = await fetch(`${API_BASE_URL}/client/${client_id}`, {
      method: "DELETE",
    });

    if (response.ok) {
      alert("Client deleted successfully!");
      fetchClients();
    } else if (response.status === 404) {
      alert("Client not found. It may have been already deleted.");
    } else {
      alert(
        `Failed to delete client. Status: ${response.status} - ${response.statusText}`
      );
    }
  } catch (error) {
    console.error("Error deleting client:", error);
  }
}

// GET de todos os employees
async function getEmployees() {
  try {
    const response = await fetch(`${API_BASE_URL}/employee/`);
    if (!response.ok) {
      throw new Error(`API error: ${response.status} - ${response.statusText}`);
    }
    return await response.json();
  } catch (error) {
    console.error("Error fetching employees:", error);
    return [];
  }
}

// Apagar employee
async function deleteEmployee(employee_id) {
  try {
    const response = await fetch(`${API_BASE_URL}/employee/${employee_id}`, {
      method: "DELETE",
    });

    if (response.ok) {
      alert("Employee deleted successfully!");
      fetchEmployees();
    } else if (response.status === 404) {
      alert("Employee not found. It may have been already deleted.");
    } else {
      alert(
        `Failed to delete employee. Status: ${response.status} - ${response.statusText}`
      );
    }
  } catch (error) {
    console.error("Error deleting employee:", error);
  }
}

async function getWorks() {
  try {
    const response = await fetch(`${API_BASE_URL}/work/`);
    if (!response.ok) {
      throw new Error(`API error: ${response.status} - ${response.statusText}`);
    }
    return await response.json();
  } catch (error) {
    console.error("Error fetching works:", error);
    return [];
  }
}

// Apagar work
async function deleteWork(work_id) {
  try {
    const response = await fetch(`${API_BASE_URL}/work/${work_id}`, {
      method: "DELETE",
    });

    if (response.ok) {
      alert("Work deleted successfully!");
      fetchWorks();
    } else if (response.status === 404) {
      alert("Work not found. It may have been already deleted.");
    } else {
      alert(
        `Failed to delete work. Status: ${response.status} - ${response.statusText}`
      );
    }
  } catch (error) {
    console.error("Error deleting work:", error);
  }
}

// GET de todos os vehicles
async function getVehicles() {
  try {
    const response = await fetch(`${API_BASE_URL}/vehicle/`);
    if (!response.ok) {
      throw new Error(`API error: ${response.status} - ${response.statusText}`);
    }
    return await response.json();
  } catch (error) {
    console.error("Error fetching vehicles:", error);
    return [];
  }
}

// Apagar vehicle
async function deleteVehicle(vehicle_id) {
  try {
    const response = await fetch(`${API_BASE_URL}/vehicle/${vehicle_id}`, {
      method: "DELETE",
    });

    if (response.ok) {
      alert("Vehicle deleted successfully!");
      fetchVehicles();
    } else if (response.status === 404) {
      alert("Vehicle not found. It may have been already deleted.");
    } else {
      alert(
        `Failed to delete vehicle. Status: ${response.status} - ${response.statusText}`
      );
    }
  } catch (error) {
    console.error("Error deleting vehicle:", error);
  }
}
