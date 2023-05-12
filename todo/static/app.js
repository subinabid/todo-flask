(function () {
  "use strict";

  // Update a task as completed
  const onClick = async (e) => {
    const url = `tasks/${e.target.dataset.id}`;
    const resp = await fetch(url, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ completed: e.target.checked }),
    });
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

  // Update task date
  const onDateChange = async (e) => {
    const url = `tasks/${e.target.dataset.id}/changedate`;
    const resp = await fetch(url, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ date: e.target.value }),
    });
    e.target.readOnly = true;
    e.target.classList.add("ne-text");
  };

  // Update task description
  const onTaskChange = async (e) => {
    const url = `tasks/${e.target.dataset.id}/changetask`;
    const resp = await fetch(url, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ task: e.target.value }),
    });
    e.target.readOnly = true;
    e.target.classList.add("ne-text");
  };

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

  const app = () => {
    let checks = document.querySelectorAll("input[type=checkbox]");
    let deletes = document.querySelectorAll("i.tc-del");
    let dates = document.querySelectorAll("input[type=date]");
    let texts = document.querySelectorAll("input[type=text]");

    for (const box of checks) {
      box.addEventListener("click", onClick);
    }

    for (const del of deletes) {
      del.addEventListener("click", onClickDel);
    }
    for (const date of dates) {
      date.addEventListener("change", onDateChange);
      date.addEventListener("dblclick", makeEditable);
    }

    for (const task of texts) {
      task.addEventListener("change", onTaskChange);
      task.addEventListener("dblclick", makeEditable);
      task.addEventListener("keypress", makeEditableOnEnter);
    }
  };

  window.addEventListener("load", app);
})();
