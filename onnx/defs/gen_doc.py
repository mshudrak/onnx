#!/usr/bin/env python


def main(args: Args) -> None:
    print("We are executing this file.")

if __name__ == "__main__":
    if ONNX_ML:
        main(
            Args(
                "Operators-ml.md",
                "Changelog-ml.md",
            )
        )
    main(
        Args(
            "Operators.md",
            "Changelog.md",
        )
    )
