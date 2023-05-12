(function () {
  "use strict";

  const onClick = async (e) => {
    const url = `tasks/${e.target.dataset.id}`;
    const resp = await fetch(url, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ completed: e.target.checked }),
    });
  };

  const onClickEdit = (e) => {
    const tid = e.target.dataset.id;
    const t = document.getElementById("tt-" + tid);
    t.readOnly = false;
    t.classList.remove("ne-text");
    const d = document.getElementById("td-" + tid);
    d.readOnly = false;
    d.classList.remove("ne-text");
  };

  const onClickDel = async (e) => {
    const url = `tasks/${e.target.dataset.id}`;
    const resp = await fetch(url, {
      method: "DELETE",
    });
    window.location.href = "/";
  };

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

  const makeEditable = (e) => {
    console.log("Dbl clicked");
    e.target.readOnly = false;
    e.target.classList.remove("ne-text");
  };

  const app = () => {
    let checks = document.querySelectorAll("input[type=checkbox]");
    let edits = document.querySelectorAll("i.tc-edit");
    let deletes = document.querySelectorAll("i.tc-del");
    let dates = document.querySelectorAll("input[type=date]");
    let texts = document.querySelectorAll("input[type=text]");

    for (const box of checks) {
      box.addEventListener("click", onClick);
    }

    for (const edit of edits) {
      edit.addEventListener("click", onClickEdit);
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
    }
  };

  window.addEventListener("load", app);
})();
