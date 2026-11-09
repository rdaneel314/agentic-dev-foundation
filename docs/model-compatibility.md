# Future rented-GPU compatibility

Keep `agent → model gateway → provider adapter → hosted API or future inference endpoint`. No GPU server, model download, paid API call or provider credential is part of this scaffold.

The future request contract should carry task and role IDs, messages, output schema, context/output token limits, timeout, retry bound, approved data class and a task cost reservation. Return text/structured output, finish reason, usage, latency, provider/model/version and a sanitized error. Store endpoint configuration and secret references outside source and prompts.

Adapters must declare capabilities: structured outputs, tools, streaming, cancellation, tokenizer/context behavior, concurrency and usage reporting. An API described as OpenAI-compatible does not guarantee equivalent tools or schemas; run contract tests before enabling a route. A generic self-hosted inference server may implement the endpoint later; no specific engine version or model license is assumed compatible.

Route changes must preserve independent reviewer contexts and identity controls. Do not silently fall back to a provider that violates data or budget policy. Fail closed when usage, reservations, authentication or required capabilities are unavailable. No real prompts or secrets in public telemetry.

Before GPU rental, measure quality, tokens, latency and utilization; compare total cost including idle time, disks, network, setup and cleanup. Verify model license, provenance, memory requirements and task quality. Require authenticated private connectivity, temporary access, bounded uptime, concurrency limits and teardown of billable residuals. Human approval of exact rental scope and cost is mandatory. This preserves an option without provisioning it.
