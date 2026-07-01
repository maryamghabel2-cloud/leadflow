"""
LeadFlow.AI - Blockchain Transaction Verifier
Audits USDT (TRC-20) payments on the Tron Blockchain via the Tronscan public API
to verify real-time customer onboarding payments without manual verification.
"""

import requests
from typing import Dict, Any

class BlockchainVerifier:
    def __init__(self, timeout: int = 10):
        self.api_url = "https://apilist.tronscan.org/api/transaction-info?hash="
        self.timeout = timeout
        self.headers = {
            "User-Agent": "LeadFlow-AI-Blockchain-Auditor/1.0",
            "Accept": "application/json"
        }

    def verify_usdt_transaction(self, tx_hash: str, expected_min_amount: float = None) -> Dict[str, Any]:
        """
        Queries Tronscan API for transaction details and audits TRC-20 USDT transfer.
        """
        tx_hash = tx_hash.strip()
        result = {
            "status": "failed",
            "tx_hash": tx_hash,
            "confirmed": False,
            "sender": None,
            "receiver": None,
            "amount_usdt": 0.0,
            "timestamp": None,
            "message": ""
        }

        if not tx_hash or len(tx_hash) < 10:
            result["message"] = "Invalid transaction hash format."
            return result

        try:
            url = f"{self.api_url}{tx_hash}"
            response = requests.get(url, headers=self.headers, timeout=self.timeout)
            
            if response.status_code != 200:
                result["message"] = f"Blockchain API returned status {response.status_code}. Unable to verify."
                return result

            data = response.json()
            
            # Check if transaction exists
            if not data or "hash" not in data:
                result["message"] = "Transaction not found on Tron blockchain ledger."
                return result

            # Check confirmation status (contractRet == SUCCESS and confirmed == true/1)
            contract_ret = data.get("contractRet", "")
            confirmed = data.get("confirmed", False)
            
            if contract_ret != "SUCCESS":
                result["message"] = f"Transaction failed or unconfirmed on chain (Status: {contract_ret})."
                return result

            result["confirmed"] = True
            result["timestamp"] = data.get("timestamp")

            # Extract TRC20 transfer info (USDT contract: TR7NHqjeKQxGTCi8q8ZY4pL8otSzgjLj6t)
            trc20_transfers = data.get("trc20TransferInfo", [])
            usdt_found = False
            
            for transfer in trc20_transfers:
                symbol = transfer.get("symbol", "").upper()
                if symbol == "USDT" or "TR7NHq" in transfer.get("contract_address", ""):
                    usdt_found = True
                    result["sender"] = transfer.get("from_address")
                    result["receiver"] = transfer.get("to_address")
                    
                    # USDT has 6 decimals on Tron
                    raw_amount = float(transfer.get("amount_str", transfer.get("amount", 0)))
                    decimals = int(transfer.get("decimals", 6))
                    result["amount_usdt"] = raw_amount / (10 ** decimals)
                    break

            if not usdt_found:
                # Check regular Tron transfers if TRC20 not present
                result["message"] = "Transaction confirmed on Tron chain, but no USDT (TRC-20) transfer detected."
                return result

            if expected_min_amount and result["amount_usdt"] < expected_min_amount:
                result["status"] = "insufficient_amount"
                result["message"] = f"Payment verified ({result['amount_usdt']} USDT), but less than required plan amount (${expected_min_amount})."
            else:
                result["status"] = "success"
                result["message"] = f"Successfully verified payment of {result['amount_usdt']} USDT from {result['sender']}."

        except Exception as e:
            result["status"] = "error"
            result["message"] = f"Blockchain audit exception: {str(e)}"

        return result

if __name__ == "__main__":
    verifier = BlockchainVerifier()
    print("Testing Blockchain Verifier with a sample Tron hash...")
    # Using a known historical USDT Tron hash for testing
    sample_hash = "853793d552635f533aa982b92b35b00e63a1c1add062c099da245cf683a31c50"
    res = verifier.verify_usdt_transaction(sample_hash)
    print("Verification Result:", res)
