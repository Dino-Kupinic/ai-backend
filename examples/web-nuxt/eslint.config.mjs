import withNuxt from "./.nuxt/eslint.config.mjs"
import eslintConfigPrettier from "eslint-config-prettier"

export default withNuxt(
  {
    files: ["**/*.ts", "**/*.tsx"],
    rules: {
      curly: ["warn", "multi-line"],
      eqeqeq: "error",
      yoda: "warn",
      "prefer-promise-reject-errors": ["error", { allowEmptyReject: true }],
      "array-callback-return": ["error", { allowImplicit: true }],
      "no-else-return": "warn",
      "no-console": "error",
      "no-constant-binary-expression": "error",
      "no-useless-return": "warn",
      "default-case-last": "error",
      "no-promise-executor-return": "error",
      "no-template-curly-in-string": "error",
      "no-unreachable-loop": "error",
      "no-duplicate-imports": "warn",
      "no-multiple-empty-lines": "warn",
      "no-label-var": "error",
      "no-undef-init": "warn",
      "no-unused-vars": [
        "error",
        {
          args: "after-used",
          argsIgnorePattern: "^_",
          ignoreRestSiblings: false,
          vars: "all",
          varsIgnorePattern: "^_",
        },
      ],
    },
  },
  {
    ignores: ["**/components/ui", "**/components/content", "**/lib"],
  },
  eslintConfigPrettier,
)
