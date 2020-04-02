/*
 * This JavaScript doesn't do anything. The file exists just to demonstrate
 * including static assets from the HTML in themes.
 */

/**
 * Behavior for side bar navigation links when clicked
 */
const sideBarNavigationLinks = () => {
  const elements = document.getElementsByClassName("side-bar__link");
  Array.prototype.map.call(elements, element => {
    element.onclick = () => {
      if (element.classList.contains("side-bar__link--collapsed")) {
        element.classList.remove("side-bar__link--collapsed");
        element.classList.add("side-bar__link--expanded");
        const submenu = element.parentElement.getElementsByClassName(
          "side-bar__sub-menu"
        );
        submenu[0].classList.add("side-bar__sub-menu--visible");
      } else {
        element.classList.remove("side-bar__link--expanded");
        element.classList.add("side-bar__link--collapsed");
        const submenu = element.parentElement.getElementsByClassName(
          "side-bar__sub-menu"
        );
        submenu[0].classList.remove("side-bar__sub-menu--visible");
      }
    };
  });
};

const openSideBarMenu = () => {
  const menu = document.getElementsByClassName("top-bar__item--trigger")[0];
  menu.onclick = () => {
    const appLayout = document.getElementsByClassName("app-layout")[0];
    appLayout.classList.add("app-layout--active-side-bar");
  };
};

const closeSideBarMenu = () => {
  const menu = document.getElementsByClassName("side-bar__close")[0];
  menu.onclick = () => {
    const appLayout = document.getElementsByClassName("app-layout")[0];
    appLayout.classList.remove("app-layout--active-side-bar");
  };
};

sideBarNavigationLinks();
openSideBarMenu();
closeSideBarMenu()