import streamlit as st


# --------------------------------------------------
# Global UI styles - Professional Design System
# --------------------------------------------------

def apply_global_styles():
    st.markdown(
        """
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=Poppins:wght@400;500;600;700;800&display=swap');

        :root {
            /* Educational Platform Color Palette - Professional & Trustworthy */
            --primary: #6366f1;
            --primary-dark: #4f46e5;
            --primary-light: #818cf8;
            --secondary: #8b5cf6;
            --accent: #06b6d4;
            --accent-dark: #0891b2;
            --success: #10b981;
            --warning: #f59e0b;
            --error: #ef4444;
            
            /* Text Colors - High Contrast for Education */
            --ink: #0f172a;
            --ink-soft: #1e293b;
            --ink-light: #475569;
            
            /* Background Colors - Clean & Academic */
            --bg-primary: #ffffff;
            --bg-secondary: #f8fafc;
            --bg-tertiary: #f1f5f9;
            
            /* Surface & Cards - Professional */
            --card-bg: rgba(255, 255, 255, 0.9);
            --card-border: rgba(99, 102, 241, 0.15);
            --card-shadow: rgba(99, 102, 241, 0.08);
            --card-shadow-hover: rgba(99, 102, 241, 0.15);
            
            /* Educational Gradients */
            --gradient-primary: linear-gradient(135deg, #6366f1 0%, #8b5cf6 50%, #06b6d4 100%);
            --gradient-accent: linear-gradient(135deg, #818cf8 0%, #6366f1 50%, #4f46e5 100%);
            --gradient-bg: linear-gradient(135deg, #e0e7ff15 0%, #ede9fe15 50%, #cffafe15 100%);
            --gradient-educational: linear-gradient(135deg, #e0e7ff 0%, #ede9fe 25%, #f3e8ff 50%, #e9d5ff 75%, #ddd6fe 100%);
        }

        /* Base App Styling - Beautiful Educational Gradient Theme */
        .stApp {
            background: 
                radial-gradient(ellipse 1800px 1200px at 0% 0%, rgba(224, 231, 255, 0.4), transparent 60%),
                radial-gradient(ellipse 1600px 1000px at 100% 0%, rgba(237, 233, 254, 0.35), transparent 60%),
                radial-gradient(ellipse 1400px 900px at 0% 100%, rgba(207, 250, 254, 0.3), transparent 60%),
                radial-gradient(ellipse 1200px 800px at 100% 100%, rgba(221, 214, 254, 0.35), transparent 60%),
                radial-gradient(ellipse 1000px 700px at 50% 20%, rgba(139, 92, 246, 0.15), transparent 70%),
                radial-gradient(ellipse 800px 600px at 20% 80%, rgba(99, 102, 241, 0.12), transparent 70%),
                linear-gradient(135deg, rgba(224, 231, 255, 0.4) 0%, rgba(237, 233, 254, 0.35) 20%, rgba(243, 232, 255, 0.3) 40%, rgba(233, 213, 255, 0.35) 60%, rgba(221, 214, 254, 0.4) 80%, rgba(207, 250, 254, 0.3) 100%),
                linear-gradient(180deg, #ffffff 0%, #f8fafc 30%, #f1f5f9 70%, #e2e8f0 100%);
            background-attachment: fixed;
            color: var(--ink);
            font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
            line-height: 1.6;
            min-height: 100vh;
        }

        /* Smooth Animations */
        section.main > div {
            animation: fadeInUp 0.6s cubic-bezier(0.16, 1, 0.3, 1);
        }

        @keyframes fadeInUp {
            from { 
                opacity: 0; 
                transform: translateY(20px); 
            }
            to { 
                opacity: 1; 
                transform: translateY(0); 
            }
        }

        /* Typography Hierarchy */
        h1, h2, h3, h4, h5, h6 {
            font-family: 'Poppins', 'Inter', sans-serif;
            font-weight: 700;
            color: var(--ink);
            letter-spacing: -0.02em;
            line-height: 1.2;
        }

        h1 {
            font-size: 3rem !important;
            font-weight: 800 !important;
            color: var(--ink) !important;
            margin-bottom: 1rem !important;
            letter-spacing: -0.03em;
        }

        h2 {
            font-size: 2.25rem !important;
            font-weight: 700 !important;
            color: var(--ink) !important;
            margin-top: 2rem !important;
            margin-bottom: 1rem !important;
        }

        h3 {
            font-size: 1.75rem !important;
            font-weight: 600 !important;
            color: var(--ink) !important;
            margin-top: 1.5rem !important;
            margin-bottom: 0.75rem !important;
        }

        h4 {
            font-size: 1.25rem !important;
            font-weight: 600 !important;
            color: var(--ink-soft) !important;
        }

        p, li, .stMarkdown, .stCaption, .stText {
            color: var(--ink);
            font-family: 'Inter', sans-serif;
            font-size: 1rem;
            line-height: 1.7;
        }

        .stMarkdown p {
            margin-bottom: 1rem;
        }

        /* Buttons - Educational Theme */
        .stButton > button {
            background: var(--gradient-primary);
            color: white !important;
            border: none;
            border-radius: 12px;
            padding: 0.75rem 1.5rem;
            font-weight: 600;
            font-size: 0.95rem;
            font-family: 'Inter', sans-serif;
            box-shadow: 0 4px 14px rgba(99, 102, 241, 0.35);
            transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
            letter-spacing: 0.01em;
        }

        .stButton > button:hover {
            transform: translateY(-2px);
            box-shadow: 0 8px 24px rgba(99, 102, 241, 0.45);
            filter: brightness(1.05);
            background: linear-gradient(135deg, #818cf8 0%, #6366f1 50%, #4f46e5 100%);
        }

        .stButton > button:active {
            transform: translateY(0);
        }

        button[kind="secondary"] {
            background: var(--bg-primary) !important;
            color: var(--primary-dark) !important;
            border: 2px solid var(--primary) !important;
            border-radius: 12px !important;
            padding: 0.75rem 1.5rem !important;
            font-weight: 600 !important;
            box-shadow: 0 2px 8px rgba(99, 102, 241, 0.15) !important;
            transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1) !important;
        }

        button[kind="secondary"]:hover {
            background: var(--gradient-primary) !important;
            color: white !important;
            transform: translateY(-2px);
            box-shadow: 0 6px 16px rgba(99, 102, 241, 0.3) !important;
            border-color: var(--primary-dark) !important;
        }

        button[kind="primary"] {
            background: var(--gradient-primary) !important;
        }

        /* Form Inputs - Clean & Modern */
        div[data-testid="stTextInput"] input,
        div[data-testid="stTextArea"] textarea,
        div[data-testid="stNumberInput"] input,
        div[data-testid="stSelectbox"] select {
            border-radius: 12px;
            border: 2px solid rgba(99, 102, 241, 0.15);
            padding: 0.75rem 1rem;
            background: rgba(255, 255, 255, 0.95);
            font-family: 'Inter', sans-serif;
            font-size: 0.95rem;
            transition: all 0.3s ease;
            box-shadow: 0 1px 3px rgba(99, 102, 241, 0.05);
        }

        div[data-testid="stTextInput"] input:focus,
        div[data-testid="stTextArea"] textarea:focus,
        div[data-testid="stNumberInput"] input:focus,
        div[data-testid="stSelectbox"] select:focus {
            border-color: var(--primary);
            box-shadow: 0 0 0 3px rgba(99, 102, 241, 0.1), 0 4px 12px rgba(99, 102, 241, 0.08);
            outline: none;
        }

        div[data-testid="stTextInput"] label,
        div[data-testid="stSelectbox"] label,
        div[data-testid="stRadio"] label,
        div[data-testid="stCheckbox"] label {
            color: var(--ink-soft);
            font-weight: 500;
            font-family: 'Inter', sans-serif;
            font-size: 0.9rem;
        }

        /* Containers & Cards - Elevated Design */
        div[data-testid="stContainer"] {
            background: rgba(255, 255, 255, 0.92);
            backdrop-filter: blur(10px);
            border: 1px solid rgba(99, 102, 241, 0.12);
            border-radius: 16px;
            padding: 1.5rem;
            box-shadow: 0 2px 12px rgba(99, 102, 241, 0.06);
            transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
            margin-bottom: 1rem;
        }

        div[data-testid="stContainer"]:hover {
            transform: translateY(-4px);
            box-shadow: 0 8px 24px rgba(99, 102, 241, 0.12);
            border-color: rgba(99, 102, 241, 0.25);
            background: rgba(255, 255, 255, 0.98);
        }

        /* Expanders */
        div[data-testid="stExpander"] {
            border-radius: 12px;
            border: 1px solid rgba(99, 102, 241, 0.12);
            background: rgba(255, 255, 255, 0.9);
            box-shadow: 0 2px 8px rgba(99, 102, 241, 0.05);
            margin-bottom: 1rem;
        }

        div[data-testid="stExpander"] > div {
            border-radius: 12px;
        }

        /* Sidebar */
        div[data-testid="stSidebar"] {
            background: linear-gradient(180deg, rgba(255, 255, 255, 0.95) 0%, rgba(248, 250, 252, 0.95) 100%);
            border-right: 1px solid rgba(99, 102, 241, 0.12);
            box-shadow: 2px 0 12px rgba(99, 102, 241, 0.05);
        }

        /* Links */
        a {
            color: var(--primary);
            text-decoration: none;
            font-weight: 500;
            transition: color 0.2s ease;
        }

        .stMarkdown a:hover {
            color: var(--primary-dark);
            text-decoration: underline;
        }

        /* Tabs */
        .stTabs [role="tablist"] {
            border-bottom: 2px solid var(--card-border);
            margin-bottom: 1.5rem;
        }

        .stTabs [role="tablist"] button {
            border-radius: 8px 8px 0 0;
            padding: 0.75rem 1.25rem;
            border: none;
            font-weight: 500;
            font-family: 'Inter', sans-serif;
            color: var(--ink-light);
            transition: all 0.2s ease;
        }

        .stTabs [role="tablist"] button[aria-selected="true"] {
            background: transparent;
            color: var(--primary-dark);
            border-bottom: 3px solid var(--primary);
            font-weight: 600;
        }

        .stTabs [role="tablist"] button:hover {
            color: var(--primary-dark);
            background: rgba(249, 115, 22, 0.08);
        }

        /* Alerts & Messages */
        .stAlert {
            border-radius: 12px;
            border: none;
            box-shadow: 0 4px 12px rgba(15, 23, 42, 0.08);
            padding: 1rem 1.25rem;
        }

        .stSuccess {
            background: rgba(16, 185, 129, 0.1);
            border-left: 4px solid var(--success);
        }

        .stError {
            background: rgba(239, 68, 68, 0.1);
            border-left: 4px solid var(--error);
        }

        .stWarning {
            background: rgba(245, 158, 11, 0.1);
            border-left: 4px solid var(--warning);
        }

        .stInfo {
            background: rgba(224, 231, 255, 0.3);
            border-left: 4px solid var(--primary);
        }

        /* Caption & Small Text */
        .stCaption {
            font-size: 0.875rem;
            color: var(--ink-light);
            font-family: 'Inter', sans-serif;
        }

        /* Dividers */
        hr {
            border: none;
            border-top: 1px solid var(--card-border);
            margin: 2rem 0;
        }

        /* Radio & Checkbox */
        .stRadio > div > label,
        .stCheckbox > label {
            font-family: 'Inter', sans-serif;
            color: var(--ink-soft);
        }

        /* Tables */
        .stDataFrame,
        table {
            border-radius: 12px;
            overflow: hidden;
            box-shadow: 0 2px 8px rgba(15, 23, 42, 0.06);
        }

        /* Code Blocks */
        code {
            background: rgba(224, 231, 255, 0.4);
            padding: 0.2rem 0.5rem;
            border-radius: 6px;
            font-family: 'Monaco', 'Courier New', monospace;
            font-size: 0.9em;
            color: var(--primary-dark);
            border: 1px solid rgba(99, 102, 241, 0.2);
        }

        pre {
            background: rgba(224, 231, 255, 0.3);
            padding: 1rem;
            border-radius: 12px;
            border: 1px solid rgba(99, 102, 241, 0.15);
            overflow-x: auto;
        }

        /* Page Links */
        .stPageLink {
            transition: all 0.2s ease;
        }

        .stPageLink:hover {
            transform: translateX(4px);
        }

        /* Custom Scrollbar */
        ::-webkit-scrollbar {
            width: 8px;
            height: 8px;
        }

        ::-webkit-scrollbar-track {
            background: var(--bg-secondary);
        }

        ::-webkit-scrollbar-thumb {
            background: var(--card-border);
            border-radius: 4px;
        }

        ::-webkit-scrollbar-thumb:hover {
            background: var(--ink-light);
        }

        </style>
        """,
        unsafe_allow_html=True,
    )
