from crem.import_env_to_db import main


def test_import_env_to_db():
    main(
        input_fname="./r2_unique_with_id.txt",
        output_fname="/tmp/out.db",
        radius=2,
        ncpu=1,
        verbose=True,
    )
