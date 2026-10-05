import streamlit as st
import ast

st.set_page_config(
    page_title="AI Code Reviewer",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 AI Code Reviewer")
st.write("Detect bugs, explain code, and suggest improvements.")

code = st.text_area(
    "Paste your code here:",
    height=350,
    placeholder="Paste your Python code here..."
)

if st.button("🔍 Review Code"):

    if not code.strip():
        st.warning("Please paste some code first.")

    else:
        st.subheader("📝 Code Review")

        # Syntax checking
        try:
            tree = ast.parse(code)

            st.success("✅ No Python syntax errors found.")

            # Basic code analysis
            issues = []

            for node in ast.walk(tree):

                # Detect division by zero
                if isinstance(node, ast.BinOp) and isinstance(node.op, ast.Div):
                    if isinstance(node.right, ast.Constant) and node.right.value == 0:
                        issues.append(
                            "⚠️ Division by zero detected."
                        )

                # Detect print statements
                if isinstance(node, ast.Call):
                    if isinstance(node.func, ast.Name):
                        if node.func.id == "print":
                            issues.append(
                                "💡 Consider using logging instead of print() "
                                "in production applications."
                            )

            if issues:
                st.subheader("🐛 Issues Found")

                for issue in issues:
                    st.write(issue)

            else:
                st.success("🎉 No obvious issues found.")

            st.subheader("💡 Suggestions")

            suggestions = [
                "Use meaningful variable and function names.",
                "Add comments or docstrings for important functions.",
                "Handle possible exceptions with try/except where appropriate.",
                "Keep functions small and focused on one task."
            ]

            for suggestion in suggestions:
                st.write("• " + suggestion)

            st.subheader("📖 Explanation")
            st.write(
                "The code was successfully parsed and basic Python "
                "syntax and common issues were checked."
            )

        except SyntaxError as error:
            st.error("❌ Syntax Error Found")

            st.write(
                f"Line {error.lineno}: {error.msg}"
            )

            st.subheader("💡 Suggestion")
            st.write(
                "Check the indicated line for missing brackets, "
                "colons, indentation, or other Python syntax problems."
            )
