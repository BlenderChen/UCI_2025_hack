import{defineConfig} from "vite";
import react from "@vitejs/plugin-react-swc";

export default defineConfig({
    plugins : [react()],
    server : {
        proxy : {
            "/time" : "http://127.0.0.1:5000", // Proxy requests to Flask backend
        },
    },
});