// React component - ScrollToTop

class ScrollToTop extends React.Component {
  componentDidUpdate() {
    let elmnt = document.querySelector("body");
    elmnt.scrollIntoView({
      behavior: "smooth",
      block: "start"
    });
  }

  render() {
    return this.props.children;
  }
}