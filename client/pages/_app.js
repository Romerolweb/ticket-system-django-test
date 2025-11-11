import '../styles/globals.css'
import Layout from '../components/Layout'

/**
 * The main App component for the Next.js application.
 *
 * This component wraps all pages in the application with a common layout.
 * It also imports the global CSS styles.
 *
 * @param {object} props - The properties for the component.
 * @param {React.ComponentType} props.Component - The page component to be rendered.
 * @param {object} props.pageProps - The properties for the page component.
 * @returns {JSX.Element} The rendered App component.
 */
export default function App({ Component, pageProps }) {
  return (
    <Layout>
      <Component {...pageProps} />
    </Layout>
  )
}
