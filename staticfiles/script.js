hljs.highlightAll();

const copyCode = (e) => {
  const code = e.nextSibling.textContent;
  navigator.clipboard
    .writeText(code)
    .then(() => {
      e.textContent = "Copied";
      setTimeout(() => {
        e.textContent = "Copy";
      }, 1000);
    })
    .catch(() => {
      alert("Failed to copy the code");
    });
};
