from os import environ, walk

from typing import Dict, Optional
import click
import clx.xms

from input_output import parse_phone_book


@click.command()
@click.option("--phone_book_path", help="Path to phone number input file")
@click.option("--run_id", default=None, help="id/timestamp of the generated result. E.g 20211120T231238")
@click.option("--dry_run", "-d", is_flag=True)
def main(phone_book_path: str, run_id: Optional[str], dry_run: bool) -> None:

    phones: Dict[str, str] = parse_phone_book(phone_book_path) 

    client: clx.xms.Client = clx.xms.Client(environ["SINCH_SERVICE_PLAN"], environ["SINCH_API_TOKEN"])

    batch_params = clx.xms.api.MtBatchTextSmsCreate()
    batch_params.sender = "Jultomten"
    batch_params.recipients = set(phones.keys())
    batch_params.body = "${message}"

    message_dict: Dict[str, str] = {}
    run_id: str = max(next(walk("output"))[1]) if run_id is None else run_id
    for nr, name in phones.items():
        with open(f"output/{run_id}/files_to_send/{name}.txt", "r") as f:
            message_str = f.read()
        message_dict[nr] = message_str

    batch_params.parameters['message'] = message_dict

    print(f"run_id: {run_id}")
    print(f"message_dict: {batch_params.parameters['message']}")
    print(f"recipients: {batch_params.recipients}")
    if dry_run:
        client.create_batch_dry_run(batch_params)

    else: 
        run_input: str = input("Are you sure you want to send SMS messsages?! [y/n]")
        if run_input.lower() == "y":
            client.create_batch(batch_params)

if __name__ == '__main__':
    main()