from fastmcp import FastMCP

def mount_servers(mcp):
    """
    Mount MCP servers from a JSON configuration file.
    
    Args:
        mcp: The MCP instance to mount servers to
        config_path: Path to the JSON configuration file
    
    Returns:
        The mcp instance with mounted servers
    """

    config = {
        "mcpServers": {
            "reporter": {
                "url": "https://nih-reporter-mcp-server-relaxed-bilby-co.app.cloud.gov/mcp",
                "transport": "http"
            },
        }
    }

    composite_proxy = FastMCP.as_proxy(config, name="Composite Proxy")
    mcp.mount(composite_proxy)

    
    
    return mcp