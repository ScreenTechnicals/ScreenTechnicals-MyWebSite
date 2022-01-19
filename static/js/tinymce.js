let script = document.createElement("script");
script.type = "text/javascript";
script.src =
  "https://cdn.tiny.cloud/1/p8ro8yv5hv3nfwepgkf6lroevucffspdcd39o25b6bkecpwk/tinymce/5/tinymce.min.js";
document.head.appendChild(script);
script.onload = function () {
  tinymce.init({
    selector: "#id_content",
    height: 600,

    plugins:
      "a11ychecker advcode casechange export formatpainter linkchecker autolink lists checklist media mediaembed pageembed permanentpen powerpaste table advtable tinycomments tinymcespellchecker codesample link image codelink code",
    toolbar:
      "a11ycheck addcomment showcomments casechange checklist code export formatpainter pageembed permanentpen table",
    toolbar_mode: "floating",
    tinycomments_mode: "embedded",
    tinycomments_author: "Author name",
    selector: "textarea", // change this value according to your HTML
    codesample_languages: [
      { text: "HTML/XML", value: "markup" },
      { text: "JavaScript", value: "javascript" },
      { text: "CSS", value: "css" },
      { text: "PHP", value: "php" },
      { text: "Ruby", value: "ruby" },
      { text: "Python", value: "python" },
      { text: "Java", value: "java" },
      { text: "C", value: "c" },
      { text: "C#", value: "csharp" },
      { text: "C++", value: "cpp" },
    ],
    toolbar: "code codesample link codelink image ",
    menubar: true,
  });
};
