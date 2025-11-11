import Header from './Header'

/**
 * A layout component that wraps the main content of the application.
 *
 * This component includes the main header and renders the children components
 * passed to it.
 *
 * @param {object} props - The properties for the component.
 * @param {React.ReactNode} props.children - The child components to be rendered.
 * @returns {JSX.Element} The rendered layout component.
 */
const Layout = ({ children }) => {
  return (
    <div>
      <Header />
      {children}
    </div>
  )
}

export default Layout