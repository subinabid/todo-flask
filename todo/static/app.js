(function () {
  "use strict";

  const onClick = async (e) => {
    console.log(e.target.checked, e.target.dataset.id);
    const url = `tasks/${e.target.dataset.id}`;
    const resp = await fetch(url, {
      method: "POST",
      body: JSON.stringify({ completed: e.target.checked }),
    });
  };

  const app = () => {
    let checks = document.querySelectorAll("input[type=checkbox]");

    for (const box of checks) {
      box.addEventListener("click", onClick);
    }
  };

  window.addEventListener("load", app);
})();
