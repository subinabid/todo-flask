(function () {
  "use strict";

  // Make an item editable
  const makeEditable = (e) => {
    e.target.readOnly = false;
    e.target.classList.remove("ne-text");
  };

  const makeEditableOnEnter = (e) => {
    if (e.key === "Enter") {
      makeEditable(e);
    }
  };

  // Update a task as completed
  const onClickComplete = async (e) => {
    const url = `tasks/${e.target.dataset.id}`;
    const resp = await fetch(url, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ completed: e.target.checked }),
    });
  };

  // Update task description
  const onTaskChange = async (e) => {
    const url = `tasks/${e.target.dataset.id}`;
    const resp = await fetch(url, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ task: e.target.value }),
    });
    e.target.readOnly = true;
    e.target.classList.add("ne-text");
  };

  // Update task date
  const onDateChange = async (e) => {
    const url = `tasks/${e.target.dataset.id}`;
    const resp = await fetch(url, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ date: e.target.value }),
    });
    e.target.readOnly = true;
    e.target.classList.add("ne-text");
  };

  // Archive a task
  const onClickArchive = async (e) => {
    const url = `tasks/${e.target.dataset.id}`;
    const resp = await fetch(url, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ archive: true }),
    });
    window.location.href = "/";
  };

  // Delete a task
  // Add a confirmation message?
  const onClickDel = async (e) => {
    const url = `tasks/${e.target.dataset.id}`;
    const resp = await fetch(url, {
      method: "DELETE",
    });
    window.location.href = "/";
  };

  const app = () => {
    let checks = document.querySelectorAll("input[type=checkbox]");
    let texts = document.querySelectorAll("input[type=text]");
    let dates = document.querySelectorAll("input[type=date]");
    let deletes = document.querySelectorAll("i.tc-del");
    let archives = document.querySelectorAll("i.tc-archive");

    for (const box of checks) {
      box.addEventListener("click", onClickComplete);
    }

    for (const task of texts) {
      task.addEventListener("change", onTaskChange);
      task.addEventListener("dblclick", makeEditable);
      task.addEventListener("keypress", makeEditableOnEnter);
    }

    for (const date of dates) {
      date.addEventListener("change", onDateChange);
      date.addEventListener("dblclick", makeEditable);
    }

    for (const del of deletes) {
      del.addEventListener("click", onClickDel);
    }

    for (const arc of archives) {
      arc.addEventListener("click", onClickArchive);
    }
  };

  window.addEventListener("load", app);
})();
